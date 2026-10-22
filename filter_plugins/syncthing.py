"""Ansible filter for the syncthing role.

Syncthing writes devices in config.xml sorted by their binary ID. The IDs are
base32, whose alphabet runs A-Z and then 2-7. Rendering in any other order
than Syncthing's own means every provision run rewrites config.xml and
restarts the container for nothing.

Mapping 2-7 to a-f gives a string that sorts in base32 order: the lowercase
letters sort after A-Z, IDs never contain lowercase, and the dashes sit in the
same positions in every ID.
"""

_BASE32_ORDER = str.maketrans("234567", "abcdef")


def syncthing_device_sort(devices):
    """Sort devices in the order used by Syncthing's base32 IDs."""
    return sorted(devices, key=lambda d: d["id"].translate(_BASE32_ORDER))


class FilterModule:
    """Register Syncthing-related Ansible filters."""

    # Ansible filter plugins expose only this required public method.
    # pylint: disable=too-few-public-methods
    def filters(self):
        """Return the Syncthing-related filters available to Ansible."""
        return {"syncthing_device_sort": syncthing_device_sort}
