# High Level Analyzer
# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions

from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, ChoicesSetting

# Custom Imports
from pprint import pprint

# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):
    # List of settings that a user can set for this High Level Analyzer.
    partFromMsgToPlot = ChoicesSetting(choices=('CPW-DATA', 'CPW-nEnW', 'CPW-CRC6', 'SPW-DATA', 'SPW-nEnW', 'SPW-LC', 'SPW-CRC16'))

    # An optional list of types this analyzer produces, providing a way to customize the way frames are displayed in Logic 2.
    result_types = {
        'part': {
            'format': 'Found: {{data.input_type}} - {{data.value}}'
        }
    }

    def __init__(self):
        '''
        Initialize HLA.

        Settings can be accessed using the same name used above.
        '''

        print("Settings:", self.partFromMsgToPlot)

    def decode(self, frame: AnalyzerFrame):
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.

        The type and data values in `frame` will depend on the input analyzer.
        '''
        if frame.type == self.partFromMsgToPlot:
            return AnalyzerFrame('part', frame.start_time, frame.end_time, {'input_type': frame.type, 'value': frame.data['value']})
