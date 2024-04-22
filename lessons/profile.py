"""Practice writing a Twitter profile class."""

class Profile:

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create new profile."""
        self.username = username_input
        self.private = True
        #return self
    
    def tweet(self, msg: str) -> None:
        """If Profile is NOT private, print msg."""
        if self.private is False:  #if not self.private:
            print(msg)

# instatiation
user1: Profile = Profile("110_rulez") #__init__
user1.private = False
user1.tweet("OOP is")
