# Coin & Purse Gateway ![MoneyBag](./img/moneybag.png)

## Overview

Service which acts as the external api gateway for the app.

## Docker image build command

### Local build
```Bash
docker build -t coin_and_purse_gateway:0.1.0 .
```

## Image run command
This should primarily be deployed with the docker-compose file in the
[app repo.](https://github.com/Drewan-Tech/coin_and_purse_app)

Following is an example of a direct run command.
* Note: This requires a previously deployed network _appnet_.
```Bash
docker run --rm --network appnet -p 80:8080 coin_and_purse_gateway:0.1.0
```

## Versions

| Version | Comment|
| ---:|:---|
| 0.1.0 | Python flask implementation of route forwarding to ledger and browser client services. |
