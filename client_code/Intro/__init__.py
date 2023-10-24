from ._anvil_designer import IntroTemplate
from anvil import *

class Intro(IntroTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_doctor_click(self, **event_args):
    open_form('DoctorLogin')
    pass

  def button_patient_click(self, **event_args):
    open_form('PatientLogin')
    pass


