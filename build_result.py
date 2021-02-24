import dataclasses as dc
from datetime import datetime, timezone

@dc.dataclass(unsafe_hash=True)
class build_result:
    start_time: datetime
    result: str

    def get_result_text(self):
        text = ''
        if self.result == 'succeeded': 
            text = 'Congrats mate! Your build as succeeded! Your mom must be proud!'
        elif self.result == 'canceled':    
            text = 'oH shoots! Someone cancelled your build!'
        elif self.result == 'failed':
            text = 'Darn the heck! Everybody fail the first time!!'
        elif self.result == 'partiallySucceeded':
            text = 'Part of your build did succeeded... but we are here for the whole shabang!'
        else:
            text = 'Seems like Azure pulled a new result out of its pants...'
        
        return text
    
    def get_running_time(self):
        delta = datetime.now(timezone.utc) - self.start_time
        return round(delta.total_seconds() / 60, 2)