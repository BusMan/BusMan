# -*- coding: utf-8 -*-

import logging

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets

logger = logging.getLogger(__name__)


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=widgets.TextInput(attrs={
        "placeholder": "Username",
        "aria-label": "Enter Username"
    }), error_messages={
        "required": "Invalid username"
    })
    password = forms.CharField(required=True, widget=widgets.PasswordInput(attrs={
        "placeholder": "Password",
        "aria-label": "Enter Password"
    }), error_messages={
        "required": "Invalid password"
    })

    def is_valid(self):
        """Validates the username and password in the form."""
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.items():
            if f != "__all__":
                self.fields[f].widget.attrs.update({"class": "error", "placeholder": ", ".join(list(error))})
            else:
                message = "Invalid password"
                self.fields["password"].widget.attrs.update({"class": "error", "placeholder": message})

        return form
