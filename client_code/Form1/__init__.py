from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # This form's whole UI is the custom HTML/JS in theme/assets/standard-page.html.
    # No native Anvil components are used, so there is nothing else to wire up here.
    # The completion code the activity generates (QUBIT-####) is entered by the
    # student back on the Ada page, in a string-match question, not here.
