# web-application-firewall
**Advanced Security (14X040) project**

_Gregory Sedykh_

# Description
This project for the Advanced Security course demonstrates how to set up a web application firewall (WAF) using nginx, ModSecurity and the OWASP Core Rule Set (CRS) that will protect a simple Django application with an input form.

Both the WAF and the Django application are running in Docker containers.


# Installation

Add an `.env` file to the root of the project with the following variable:
```
DJANGO_SECRET_KEY=your_secret_key
```

To start the project, run the following command:
```
docker compose up
```

To test the project, go to: 
```
http://localhost/test/
```