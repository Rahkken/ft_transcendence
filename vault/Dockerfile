FROM hashicorp/vault:latest

WORKDIR /vault

RUN apk add --no-cache curl

COPY . .

RUN chmod +x /vault/entrypoint.sh

ENTRYPOINT ["/vault/entrypoint.sh"]