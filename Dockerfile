FROM python:alpine 

RUN useradd blogapi 

WORKDIR /home/blogapi 

COPY requirements.txt requirements.txt 
RUN python -m venv venv 
RUN venv/bin/pip install -r requirements.txt 
RUN venv/bin/pip install gunicorn pymysql cryptography 

COPY app app  
COPY migrations migrations  
COPY blogapi.py config.py boot.sh ./  
RUN chmod a+X boot.sh  

ENV FLASK_APP blogapi.py 

RUN chown -R blogapi:blogapi ./ 
USER blogapi  

EXPOSE 5000 
ENTRYPOINT [ "./boot.sh" ]