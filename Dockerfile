FROM python:3.12

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/sh www-user

RUN chown -R www-user:www-user /usr/src/app

USER www-user

EXPOSE 5000

CMD [ "python", "main.py" ]
