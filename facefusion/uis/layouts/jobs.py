import gradio

from facefusion import state_manager
from facefusion.uis.components import about, job_list, job_list_options


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					job_list_options.render()
			with gradio.Column(scale = 5):
				with gradio.Blocks():
					job_list.render()
	return layout


def listen() -> None:
	job_list_options.listen()
	job_list.listen()


def run(ui : gradio.Blocks) -> None:
	ui.launch(show_api = False, inbrowser = state_manager.get_item('open_browser'))