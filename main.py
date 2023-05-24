import script
from fastapi import FastAPI

app = FastAPI()


@app.get('/about')
def read_root():
    return 'no content'


script.init(app)
# web_app.init(app)

if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')