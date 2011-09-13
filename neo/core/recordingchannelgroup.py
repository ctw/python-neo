from neo.core.baseneo import BaseNeo

class RecordingChannelGroup(BaseNeo):
    """
    A RecordingChannelGroup is a container inside a Block of some RecordingChannel.
    It can be usefull for grouping channel that share something in common :
    an multielectrode array or a tetrode or EEG channel setup.
    

    Usage:
    
    
    Necessary Attributes/properties:
    
    Recommanded Attributes/properties:
        channel_names:
        channel_indexes:
    
    Container of:
        RecordingChannel
        AnalogSignalArray
        
        
        
    """
    def __init__(self, **kargs):
        BaseNeo.__init__(self, **kargs)
        self.analogsignalarrays = [ ]
        self.recordingchannels = [ ]

