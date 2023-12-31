from ._anvil_designer import DoctorSignUpTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState


class DoctorSignUp(DoctorSignUpTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def confirm_click(self, **event_args):
    AppState.Dusername=self.username_sign.text
    AppState.Dpassword=self.password_sign.text
    AppState.DName=self.nameD.text
    anvil.server.call('add_doctor', AppState.Dusername, AppState.Dpassword, AppState.DName)

    open_form('DoctorLogin')
    pass

  def dsback_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DoctorLogin')
    pass




