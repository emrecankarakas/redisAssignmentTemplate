def on_sum(sum):
  if sum > 30000:
        publish('high_sum', sum)
    else:
        publish('low_sum', sum)

subscribe('sum', on_sum)
