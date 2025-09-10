# Dictionaries #
# key:value stores
# keys must be unique
# can only use immutable objects like strings for keys
# can use both immutable and mutable objects for values
# unordered

team = {
    "John Jackson": "Director",
    "Ruby Matsumoto": "Product Manager",
    "Perlie Python": "Developer",
}

print(
    team
)  # {'John Jackson': 'Director', 'Ruby Matsumoto': 'Product Manager', 'Perlie Python': 'Developer'}

for member, role in team.items():
    print(f"{member} is a {role}")

# deleting a key-value pair

del team["Perlie Python"]

print(team)  # {'John Jackson': 'Director', 'Ruby Matsumoto': 'Product Manager'}

print(f"There are {len(team)} members in the team.")  # There are 2 members in the team.

# addomg a key-value pair

team["Caspian Cassoc"] = "QA Tester"

print(
    team
)  # {'John Jackson': 'Director', 'Ruby Matsumoto': 'Product Manager', 'Caspian Cassoc': 'QA Tester'
