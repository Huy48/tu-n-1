from flask import Flask

ungdung = Flask(__name__)

@ungdung.route("/")

def text():
	return '''
	<html>
		<head><title>Sivandla</title></head>
		<body>
			<h1>Bài 1<h1>
			<img src="/static/Figure_1.png" alt="Hình ảnh của tôi" width="300">
			<img src="/static/Screenshot 2024-09-16 164517.png" alt="Hình ảnh của tôi" width="300">
		</body>
	</html>
	'''

if __name__ == "__main__":
	ungdung.run()
