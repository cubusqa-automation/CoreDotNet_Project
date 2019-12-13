FROM python:3.7
MAINTAINER Vijay.J <vijayjeyaram@gmail.com>
COPY . /Mobile_Internet_Banking
ADD requirements.txt /Mobile_Internet_Banking/requirements.txt
RUN pip install -r /Mobile_Internet_Banking/requirements.txt
WORKDIR /Mobile_Internet_Banking/authentication
ENTRYPOINT ["pytest"]
CMD ["-v", "-s","-n 3", "--alluredir=/Mobile_Internet_Banking/Allure_Result"]