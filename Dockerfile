FROM python:alpine3.7
COPY . /flaskwebapi
WORKDIR /flaskwebapi
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]