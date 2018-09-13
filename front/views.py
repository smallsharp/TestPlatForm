# encoding=utf-8
from flask import request
from flask import render_template, redirect, url_for
from front.models import Article
from flask import session
from flask import Blueprint
from . import db
from .models import User
import requests
import json
from flask import jsonify
from . import business, urls

# front = Blueprint('front', __name__, template_folder='templates',url_prefix='/front')
front = Blueprint('front', __name__, template_folder='templates')


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/test')
def index2():
    return render_template('test.html')


@front.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('front.login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@front.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        # print("telephone:{},password:{}".format(request.args.get('phone'), request.args.get('password')))
        return render_template('login.html')
    else:
        telephone = request.form.get('phone')
        password = request.form.get('password')
        print("telephone:{},password:{}".format(telephone, password))
        # return redirect(url_for('index'))
        res = {"retCode": "200", "retMsg": "登录成功！"}
        import json
        return str(json.dumps(res, ensure_ascii=False))


@front.route('/new_article', methods=['GET', 'POST'])
def new_article():
    if request.method == 'GET':
        return render_template('new_article.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        print(title, content)

        if title and content:
            # 增加：
            import datetime
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%S:%M")
            print('当前时间%s' % now)
            article1 = Article(title=title, content=content, create_time=now)
            db.session.add(article1)
            # 事务
            db.session.commit()
            # return str({"retCode": 0, "title": title, "content": content})
            return redirect(url_for('front.article_list'))
        else:
            return str({"retCode": 1001, "retMsg": '文章标题或内容不能为空', "retData": None})


@front.route('/article_list', methods=['GET'])
def article_list():
    # 查
    # select * from article where article.title='aaa';
    art_list = Article.query.filter(Article.id >= 1)
    return render_template('art_list.html', art_list=art_list)


@front.route('/question/<islogin>')
def question(islogin):
    if islogin == '1':
        return '发布问题页面'
    return redirect(url_for('login'))


@front.route('/read_data')
def read_data():
    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = Person('miaomiao', 4)

    context = {
        'username': 'likai',
        'age': 22,
        'height': 178,
        'websites': {
            'baidu': 'www.baidu.com',
            'github': 'www.github.com'
        },
        'child': p
    }
    return render_template('read_data.html', **context)


## session

@front.route('/add_session/')
def add_session():
    session['userid'] = '8473'
    # 设置session过期时间
    session.permanent = True
    return 'add session success'


@front.route('/get_session/')
def get_session():
    userid = session.get('userid')
    if userid:
        return 'session data:%s' % userid
    return 'No session data found!'


@front.route('/delete_session/')
def delete_session():
    if session.get('userid'):
        session.pop('userid')
    return 'delete success'


@front.route('/easyui/')
def easyui():
    return render_template('easyui/easyui.html')


@front.route('/auto/')
def auto():
    return render_template('index.html')


@front.route('/model/')
def model():
    pass


@front.route('/easyui_message/')
def easyui_message():
    return render_template('easyui/messager.html')


@front.route('/easyui_panel/')
def easyui_panel():
    return render_template('easyui/easyui_panel.html')


@front.route('/boot/')
def boot():
    return render_template('boot.html')


@front.route('/suite/wx')
def suite_wx():
    return render_template('suite_wx.html')


@front.route('/suite/wx/demand/goods')
def wx_goods():
    return render_template('goods.html')


@front.route('/suite/neway')
def suite_neway():
    return render_template('suite_neway.html')


@front.route('/suite/finance')
def suite_finance():
    return render_template('suite_finance.html')


@front.route('/suite/all')
def suite_all():
    return render_template('suite_all.html')


@front.route('/suite/list/', methods=['GET', 'POST'])
def suite_list():
    return jsonify(
        {"total": 2, "rows": [{"id": 1001, "name": '登录流程测试', "comment": "登录相关流程测试描述", "createTime": "2010-08-30"},
                              {"id": 1002, "name": '发布流程测试', "comment": "发布相关流程测试描述", "createTime": "2010-09-01"}]})


@front.route('/suite/detail/', methods=['GET', 'POST'])
def suite_detail():
    print(request.url)
    print(request.args.get('id'))
    return jsonify({"total": 22, "rows": [
        {"id": 1, "suiteId": 2, "testName": "打开首页",
         "element": "com.android.packageinstaller:id/permission_allow_button",
         "index": "", "findType": "id"}]})


@front.route('/delDemands/', methods=['POST'])
def delDemands():
    openId = request.form.get('openId')
    print("openId:", openId)
    data_user = {
        "page": 1,
        "lon": 121.265562,
        "lat": 31.192338,
        "openId": openId
    }
    # 请求我的需求接口
    res_user = requests.post(urls.url_userDemand, json=data_user)
    res = json.loads(res_user.text)
    if res.get('retCode') == 0 and len(res['retData']['list']) > 0:
        for demand in res.get('retData').get('list'):
            # 获取需求id
            demandId = demand['demandId']
            data_del = {
                "id": demandId,
                "openId": openId
            }
            # 请求删除需求接口
            res_del = requests.post(urls.url_del_demand, json=data_del)
            if res_del.status_code != 200:
                continue
        return jsonify({"retCode": 0, "retMsg": "删除成功"})
    else:
        return jsonify({"retCode": 99, "retMsg": "没有找到需求"})


@front.route('/delCache')
def del_cache():
    uid = request.args.get('uid')
    print(uid)
    if uid:
        res = requests.get(urls.url_del_cache, uid)
        if res.status_code == 200:
            return jsonify({"retCode": 0, "retMsg": "success"})
        return jsonify({"retCode": 98, "retMsg": res.status_code})
    else:
        return jsonify({"retCode": 99, "retMsg": "uid不能为空"})
