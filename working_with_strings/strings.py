import pandas as pd
import re

s = pd.Series(['Avidia', 'Noobsverse', 'NBL', 'Noobs'])

print(s.str.findall('^n', flags=re.IGNORECASE))
print(s.str.findall('se$'))
print(s.str.findall('[a-n|A-N]'))
print(s.str.find('oo')) #returns 1 or -1

print(s.str.extract(r'([a])', expand=False))

"""
Regular expressions (regex) are a powerful tool for matching patterns in text. They can be used in many programming languages and tools to search, match, and manipulate strings. Here's a basic guide to some of the most common regex syntax elements along with examples.

### Basic Regex Syntax

1. **Literals**: These are the exact text matches.
   - Example: `cat` matches "cat" in "The cat is cute."

2. **Character Classes**: Match any one of the enclosed characters.
   - `[abc]` matches any one of "a", "b", or "c".
   - Example: `gr[ae]y` matches "gray" or "grey".

3. **Negated Character Classes**: Match any character not enclosed.
   - `[^abc]` matches any character except "a", "b", or "c".
   - Example: `[^0-9]` matches any non-digit character.

4. **Dot (.)**: Matches any single character, except newline characters.
   - Example: `a.c` matches "abc", "arc", "a3c", etc.

5. **Anchors**: Match positions in the text.
   - `^` matches the start of the string. `^abc` matches "abc" in "abcdef", but not in "zabcdef".
   - `$` matches the end of the string. `abc$` matches "abc" in "my abc", but not in "abc def".

6. **Quantifiers**: Specify the number of times a character, group, or character class must occur.
   - `*` (zero or more), `+` (one or more), `?` (zero or one)
   - `{n}` (exactly n times), `{n,}` (n times or more), `{n,m}` (between n and m times)
   - Example: `a{2,3}` matches "aa" or "aaa" but not "a".

7. **Escaping Special Characters**: Use `\` to treat special characters like ordinary characters.
   - Example: `\.` matches a literal dot ".".

8. **Alternation (|)**: Acts like a boolean OR.
   - Example: `cat|dog` matches "cat" or "dog".

9. **Grouping (())**: Controls the scope of alternation and can capture the text matched by the enclosed pattern.
   - Example: `(cat|dog)s?` matches "cat", "cats", "dog", and "dogs".

10. **Character Shortcuts**:
    - `\d` matches any digit, equivalent to `[0-9]`.
    - `\D` matches any non-digit, equivalent to `[^0-9]`.
    - `\w` matches any word character (letters, digits, and underscores), equivalent to `[a-zA-Z0-9_]`.
    - `\W` matches any non-word character, equivalent to `[^a-zA-Z0-9_]`.
    - `\s` matches any whitespace character (spaces, tabs, line breaks).
    - `\S` matches any non-whitespace character.

### Examples

- **Email Matching**:
  ```regex
  \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
  ```
  Matches most email formats like "name@example.com".

- **URL Matching**:
  ```regex
  https?://(?:www\.)?\w+\.\w{2,3}(?:/\S*)?
  ```
  Matches URLs starting with "http" or "https", such as "http://example.com" or "https://www.example.com/path".

- **Password Strength Check**:
  ```regex
  (?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}
  ```
  Ensures the string has at least one digit, one lowercase letter, one uppercase letter, and is at least 8 characters long.

These are just a few examples to get you started. Regular expressions can be fine-tuned to match very specific patterns and are incredibly useful in processing text data efficiently. If you want to explore more complex patterns or have specific scenarios, feel free to ask!
"""