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

## Testing

The Molecule scenario checks that `templates/config.xml.j2` renders exactly
what Syncthing itself writes. It runs the image the role deploys, makes
Syncthing save its own config, and fails with a diff if anything differs - the
usual cause being a new Syncthing release changing its config schema.

It needs Python with `ansible-core`, `molecule` and `docker` installed, and a
reachable Docker daemon. No virtual machines are involved.

```shell
pip install ansible-core molecule docker
molecule test
```

The same test runs in GitHub Actions on every push and weekly, and locally
under [act](https://github.com/nektos/act):

```shell
act workflow_dispatch -W .github/workflows/molecule.yml -j molecule
```
