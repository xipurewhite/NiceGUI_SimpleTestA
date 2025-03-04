#######################################
# 界面层
# python .\ui_layer.py
#######################################
from nicegui import ui
from nicegui import app
from orm_database import init_db
from logic_layer import validate_login, validate_register, get_user
import uvicorn

# 载入用户信息数据库
app.on_startup(init_db)

# 创建登录注册界面
def create_auth_interface() -> None:
    # 页面容器样式
    with ui.column().classes('w-full max-w-md mx-auto my-24 p-8 bg-white rounded-lg shadow-lg'):
        # 标题区
        with ui.row().classes('space-y-6'):
            ui.label('登录注册界面').classes('text-2xl font-bold text-center w-full text-gray-800')
        
        # 选项卡切换
        with ui.tabs().props('inline-label dense').classes('w-full mb-6') as tabs:
            ui.tab('登录').classes('text-gray-600')
            ui.tab('注册').classes('text-gray-600')

        # 创建选项卡组件并绑定默认值
        with ui.tab_panels(tabs, animated=True, value=tab_value).classes('w-full'):
            # 登录表单
            with ui.tab_panel('登录'):
                    username = ui.input(label='用户名', placeholder='请输入用户名')
                    username.tailwind('w-full mb-4')
                    password = ui.input(label='密码', password=True, password_toggle_button=True)
                    password.tailwind('w-full mb-6')

                    bt_login = ui.button('立即登录', on_click= lambda: _handle_login(username.value, password.value))
                    bt_login.tailwind('w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded')
            # 注册表单
            with ui.tab_panel('注册'):
                reg_username = ui.input(label='新用户名', validation={'用户名长度需要>=3': lambda v: len(v) >= 3})
                reg_username.tailwind('w-full mb-4')
                
                reg_password = ui.input(label='设置密码', password=True, validation={'密码长度需要>=3': lambda v: len(v) >= 3})
                reg_password.tailwind('w-full mb-4')
                
                confirm_password = ui.input(label='确认密码', password=True, validation={'密码长度需要>=3': lambda v: len(v) >= 3})
                confirm_password.tailwind('w-full mb-6')

                bt_regs = ui.button('立即注册', on_click=lambda: _handle_register(
                    reg_username.value, 
                    reg_password.value,
                    confirm_password.value
                ))
                bt_regs.tailwind('w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded')
# 回调：登录
async def _handle_login(username: str, password: str):
     result = await validate_login(username, password)
     ui.notify(result['info'], type=result['status'])

# 回调：注册
async def _handle_register(username: str, password: str, confirm: str):
     result = await validate_register(username, password, confirm)
     ui.notify(result['info'], type=result['status'])


# =====================================
# API: 获取当前登录用户
# Example: localhost:8080/api/getuser?username=abc
@app.get('/api/getuser')
async def api_current_user(username: str):
    return await get_user(username)


# =====================================
tab_value = '登录'  # 默认控制选项卡状态
# 初始化UI界面
create_auth_interface()
ui.run(title='登录注册界面', port=8080)
