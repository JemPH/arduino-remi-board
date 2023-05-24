import redis
from nicegui import ui, app
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

r_db = redis.Redis(
    host='zc540g.stackhero-network.com',
    port=6379,
    password='4nGDxa3Si8Q5CrkoWJLXtWbdTcp1VcTr3LsawGuMQcWWfhuMVIhJU0HkoxgYT2mt'
)

def init(app: FastAPI) -> None:
    @ui.page('/')
    def main_page(request: Request):
        def sendToRedis() -> None:
            if type.value == 'Announcement':
                r_db.set('message', announcement.value)
            elif type.value == 'Scoreboard':
                msg_data = f"{team_1_name.value} {team_1_score.value} - {team_2_name.value} {team_2_score.value}"
                r_db.set('message', msg_data)
            ui.notify('Update message.')
        with ui.card().classes('absolute-center'):
            ui.label('Remi Board').classes('font-mono').classes('self-center').classes('text-2xl')
            ui.label('\n\n\n\n')
            ui.label('Announcement Board').classes('font-mono').classes('self-center').classes('text-l')
            announcement = ui.input('Announcement').on('keydown.enter', sendToRedis).classes('w-full')
            ui.label('\n\n')
            ui.label('Score Board').classes('font-mono').classes('self-center').classes('text-l')
            team_1_name = ui.input('Team 1 Name').on('keydown.enter', sendToRedis).classes('w-full')
            team_2_name = ui.input('Team 2 Name').on('keydown.enter', sendToRedis).classes('w-full')
            with ui.row():
                team_1_score = ui.input('Add Score : Team 1').on('keydown.enter', sendToRedis).classes('w-full')
                team_2_score = ui.input('Add Score : Team 2').on('keydown.enter', sendToRedis).classes('w-full')
                
            type = ui.select(['Announcement', 'Scoreboard'], value='Announcement').on('keydown.enter', sendToRedis).classes('self-stretch')
            with ui.row().classes('w-full'):
                ui.button('Submit', on_click=sendToRedis).props('color=green').classes('w-full h-10')

    ui.run_with(app, title='Remi Board', dark=True, favicon='icon.png')