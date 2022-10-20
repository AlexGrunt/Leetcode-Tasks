class Solution:
    def findAnagrams(self, text: str, pattern: str) -> List[int]:
        if len(pattern) > len(text):
            return []

        letter_counts = defaultdict(int)

        for i in range(len(pattern)):
            letter_counts[pattern[i]] += 1
            letter_counts[text[i]] -= 1

        missed_letters_count = len(
            [value for value in letter_counts.values() if value < 0])
        anagram_positions = []

        for i in range(len(text) - len(pattern) + 1):
            if missed_letters_count == 0:
                anagram_positions.append(i)

            letter_counts[text[i]] += 1

            if letter_counts[text[i]] == 0:
                missed_letters_count -= 1

            if i + len(pattern) < len(text):
                next_letter = text[i + len(pattern)]

                letter_counts[next_letter] -= 1

                if letter_counts[next_letter] == -1:
                    missed_letters_count += 1

        return anagram_positions