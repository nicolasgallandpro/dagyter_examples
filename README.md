# dagyter_examples

This repo gives you 2 examples of [Dagyter](https://github.com/nicolasgallandpro/dagyter) projects configurations

## Example 1 : ex1_localhost_simple
### Description
This example contains a Dagyter stack (Dagster, Jupyter with basics python/pandas libs, and Streamlit) and a "Cross app menu" that allows you to have this 3 tools in the same browser tab (inside iframes), and let you switch between them with a right menu.

### Installation
Clone this project, go to the directory ex1_localhost_simple, and execute the command :
docker-compose up -d

The 'urls' file contains the configuration of the right menu. See the [cross-app-menu repo](https://github.com/nicolasgallandpro/cross-app-menu) for more explanations.

Docker will create a "persistance" directory to persist Dagster history and informations.


## Example 2 :  ex2_with_caddy_subdmains_auth_superset
### Description
Compared to example 1, example 2 has in addition :
- Apache Superset configured with a postgres database
- Caddy (reverse proxy). Caddy is pre-configured to manage domain and sub domain configuration, basic auth, and https

### Installation and configuration
Before Launching docker-compose, you have to configure domains and subdomains in urls file and configure the Caddyfile with your logins, domains, ...
The 'urls' file is used as an env file for the caddy container, so you can use 'urls' variables in the Caddyfile.

