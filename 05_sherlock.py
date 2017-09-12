def sherlock(guests):

   for guest in guests:
        if guest == "Dr Watson" and "Inspector Lestrade":
            return "Enter"
        else:
            return "Go Away! (sound of violin music...)"


def main():
    press = ["a reporter from the Times", "a reporter from the Observer"]
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]
    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))


if __name__ == "__main__":
    main()
