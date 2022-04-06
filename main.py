import webbrowser

o = open('paguntalan.html', 'w')
message = """<html>
<title>My First HTML</title>
<head></head>
<body><h1>Welcome to My First HTML Program Using Python!</h1>
<h2>My name is Xandrix Jill B. Paguntalan!</h2></body>
<p>Thank you!</p></body>
</html>"""
o.write(message)
o.close()
webbrowser.open_new_tab('paguntalan.html')