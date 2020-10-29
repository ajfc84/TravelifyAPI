FROM python
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip && \
	pip3 install django && \
	django-admin startproject example . && \
	sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['*'\]/" ./example/settings.py
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

