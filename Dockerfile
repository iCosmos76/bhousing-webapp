FROM python:3.10.10

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/bhousing_webapp

ARG PIP_EXTRA_INDEX_URL

# Install requirements
ADD ./ /opt/bhousing_webapp
RUN pip install --upgrade pip
RUN pip install -r /opt/bhousing_webapp/requirements.txt

RUN chmod +x /opt/bhousing_webapp/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
