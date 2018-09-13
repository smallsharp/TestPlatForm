from front import create_app
app = create_app()

if __name__ == '__main__':
    # 使用 python wsgi.py 启动
    # http://192.168.40.143:5000/
    app.run()
