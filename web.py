from abc import ABCMeta, abstractmethod

class jobScrapeController(metaclass=ABCMeta):
    @abstractmethod
    def fetchAJob(self):
        pass

