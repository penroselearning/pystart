url = ['https://www.penroselearning.com/test-site',
       'https://www.abclearning.com/test-site2',
       'https://www.xyzlearning.com/test-site5']

print('Extracted URL:')
print('-' * 30)
for u in url:
    start = u.find('www.')
    stop = u.find('/test')
    print(u[start:stop:1])
