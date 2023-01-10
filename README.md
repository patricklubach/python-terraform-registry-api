# terraform-registry-api

This API is intended to host a private [Terraform Registry API](https://developer.hashicorp.com/terraform/cloud-docs/api-docs/private-registry/modules#create-a-module-version) written in Python.

## Requirements

Install the requirements by running:

```bash
virtualenv venv
source venv/bin/activate
venv/bin/pip install -r requirements.txt
```

## Start

Start the server:

```bash
venv/bin/python -m registry
```

## What's missing / Roadmap

- [ ] Implement proper logging
- [ ] Implement local filesystem as backend ([SQLite](https://docs.python.org/3/library/sqlite3.html))
- [ ] Implement Terraform module VCS publishing
- [ ] Implement terraform [HTTP Status Codes](https://developer.hashicorp.com/terraform/registry/api-docs#http-status-codes)
- [ ] Implement [pagination](https://developer.hashicorp.com/terraform/registry/api-docs#pagination)
- [ ] Implement Terraform Provider endpoints
- [ ] Implement GCS as backend
- [ ] Implement SQL as backend
- [ ] Implement Terraform module no VCS publishing

## Helpful Links

- [Terraform Registry API](https://developer.hashicorp.com/terraform/registry/api-docs)
- [Terraform Registry Modules API](https://developer.hashicorp.com/terraform/cloud-docs/api-docs/private-registry/modules#publish-a-private-module-from-a-vcs) / Terraform Cloud Registry Implementation
