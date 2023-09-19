# Ansible Role: syncthing

[![Lint](https://github.com/dcjulian29/ansible-role-syncthing/actions/workflows/lint.yml/badge.svg)](https://github.com/dcjulian29/ansible-role-syncthing/actions/workflows/lint.yml) [![GitHub Issues](https://img.shields.io/github/issues-raw/dcjulian29/ansible-role-syncthing.svg)](https://github.com/dcjulian29/ansible-role-syncthing/issues)

This an Ansible role to install and configure Syncthing

## Requirements

- Active Internet Connection.

## Installation

To use, use `requirements.yml` with the following git source:

```yaml
---
roles:
- name: dcjulian29.syncthing
  src: https://github.com/dcjulian29/ansible-role-syncthing.git
  ```

Then download it with `ansible-galaxy`:

```shell
ansible-galaxy install -r requirements.yml
```

## Dependencies

- None
