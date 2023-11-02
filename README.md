

### build ###
docker build -t python-openai .

### run with mount local source ###

docker run -it --rm -v $PWD:/app  -e OPENAI_API_KEY=key --name lifmat-run python-openai /bin/bash 
python app.py


