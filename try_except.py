try:
  value = dict[key]
except:
  value = default_value
# Вместо

if dict.has_key(key):
  value = dict[key]
else:
  value = default_value
