# Basic Hello World web service 
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        # Web browsers disable CORS by default
        # enable it using this code
        web.header('Access-Control-Allow-Origin', '*')

        if not name:
            name = 'World'
        return name

if __name__ == "__main__":
    app.run()
