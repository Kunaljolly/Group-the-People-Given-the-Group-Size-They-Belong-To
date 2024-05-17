class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    d = {}
    result = []
    for i, size in enumerate(groupSizes):
      if size not in d:
        d[size] = []
      if len(d[size]) < size:  # Check if there's space in the current group
        d[size].append(i)
      else:
        result.append(d[size])  # Add existing full group to result
        d[size] = [i]  # Start a new group with only the current person

    # Add any remaining groups (including those with a single person)
    for value in d.values():
      if value:
        result.append(value)

    return result
