questions = """x = 3
x + 5
y = x
y + 3 * 2 + 5
lst = [1, 2, 3]
lst.pop()
lst.append([4,5])
lst"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-modify-public streaming playlist-read-private user-read-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def setup():
	# shuffle songs
	sp.shuffle(True)

def is_statement(s):
	""" I copied this from stackoverflow """
	isstatement= False
	try:
		code= compile(s, '<stdin>', 'eval')
	except SyntaxError:
		isstatement= True
		code= compile(s, '<stdin>', 'exec')
	return isstatement

def pose_question():
	print("What would Python Display?")
	list_questions = questions.split("\n")
	for s in list_questions:
		if is_statement(s):
			print(">>>", s)
			compile(s, '<stdin>', 'exec')
			exec(s)
		else:
			print(">>>", s)
			right_answer = str(eval(s, locals()))
			if eval(right_answer) is None:
				continue
			ans = input("")
			while str(ans) != right_answer:
				wrong_answer_music()
				print(">>>", s)
				ans = input("")
			right_answer_music()

def wrong_answer_music():
	device = get_devices()
	sp.start_playback(device_id=device,
		context_uri='spotify:playlist:0kcjupFHeaezPvQ6xfHscR')

def right_answer_music():
	device = get_devices()
	sp.start_playback(device_id=device,
		context_uri='spotify:playlist:02AJeARcWPsqcUiFNAXHXv')

def get_devices():
	for d in sp.devices()['devices']:
		if d['name'] == "Catherine's MacBook Pro":
			return d['id']
	return None

if __name__ == '__main__':
	setup()
	pose_question()
	sp.pause_playback()