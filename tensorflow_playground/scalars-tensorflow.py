import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

addExpr = tf.add(a, b)

session = tf.Session()
bindings = {a: 5.1, b: 1}

c = session.run(addExpr, feed_dict=bindings)
print(c)
