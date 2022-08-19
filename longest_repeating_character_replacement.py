class Solution(object):
    def characterReplacement(self, s, k):
        window_start = longest = max_repeating_char = 0
        window_frequency_map = {}

        for window_end in range(len(s)):
            end_char = s[window_end]

            if end_char not in window_frequency_map:
                window_frequency_map[end_char] = 0
            window_frequency_map[end_char] += 1

            max_repeating_char = max(max_repeating_char, window_frequency_map[end_char])

            if window_end - window_start + 1 - max_repeating_char > k:
                start_char = s[window_start]
                window_frequency_map[start_char] -= 1
                if window_frequency_map[start_char] == 0:
                    del window_frequency_map[start_char]
                window_start += 1

            longest = max(longest, window_end - window_start + 1)
        return longest
        