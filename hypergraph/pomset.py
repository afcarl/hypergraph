import numpy as np

def _order_bfs(order, direction='up'):
	if direction == 'up':
		
		pass
	elif direction == 'down':

		pass
	else:
		raise ValueError('bfs direction must be either "up" or "down"')

class POMSet (object):
	'''A Partially Ordered Multiset.

	A POMSet is composed of labels (the items in the multiset) and
	an order (the partial order of the labels). Partial orders are
	provided as 2 dimensional numpy ndarray specifying order relations
	on the `i`th and `j`th labels as 
		order[i,j] == 1  <==> labels[i] > label[j]
		order[i,j] == 0  <==> label[i] is unrelated to label[j]
		order[i,j] == -1 <==> label[i] < label[j]

	The `size` of a POMSet is the number of labels.
	The `support` of a POMSet is the set of distinct labels.
	The `cardinality` of a POMSet is the size of the support.
	'''

	def __init__(self, labels=None, order=None):

		if labels is not None:
			self.labels = np.array(labels, dtype=object)
		else:
			self.labels = np.array([], dtype=object)

		self.size = len(self.labels)
		self.support = set(self.labels)
		self.cardinality = len(self.support)

		if order is not None:
			assert(order.shape[0] == len(self.labels))
			self.order = order
		else:
			self.order = np.zeros((self.size, self.size), dtype=np.int8)

	def weakly_above(self, element, element_index=0):
		'''Get all elements of the POMSet that are weakly above `element`.

		Here weakly above means elements that are either strictly greater than 
		or unrelated to `element` in the POSET order.

		Parameters
		----------

		element : object
			The element of the POMSet to find elements above.

		element_index : int, optional
			In case there are multiple instances of element in the POMSet
			labels, the index of the element to find elements above;
			e.g. `element_index=3` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		labels_above : numpy ndarray
			A numpy array of label objects weakly above `element`
		'''
		label_index = np.where(self.labels == element)[0][element_index]
		return self.labels[~(self.order[label_index] == -1)]

	def _indices_strictly_above(self, element, element_index=0):
		label_index = np.where(self.labels == element)[0][element_index]
		return np.where[(self.order[label_index] == 1)][0]

	def strictly_above(self, element, element_index=0):
		'''Get all elements of the POMSet that are strictly above `element`.

		Here weakly above means elements that are strictly greater than 
		`element` in the POSET order.

		Parameters
		----------

		element : object
			The element of the POMSet to find elements above.

		element_index : int, optional
			In case there are multiple instances of element in the POMSet
			labels, the index of the element to find elements above;
			e.g. `element_index=3` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		labels_above : numpy ndarray
			A numpy array of label objects strictly above `element`
		'''
		label_index = np.where(self.labels == element)[0][element_index]
		return self.labels[(self.order[label_index] == 1)]

	def weakly_below(self, element, element_index=0):
		'''Get all elements of the POMSet that are weakly below `element`.

		Here weakly above means elements that are either strictly less than 
		or unrelated to `element` in the POSET order.

		Parameters
		----------

		element : object
			The element of the POMSet to find elements below.

		element_index : int, optional
			In case there are multiple instances of element in the POMSet
			labels, the index of the element to find elements below;
			e.g. `element_index=3` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		labels_below : numpy ndarray
			A numpy array of label objects weakly below `element`
		'''
		label_index = np.where(self.labels == element)[0][element_index]
		return self.labels[~(self.order[label_index] == 1)]

	def _indices_strictly_below(self, element, element_index=0):
		label_index = np.where(self.labels == element)[0][element_index]
		return np.where[(self.order[label_index] == -1)]

	def strictly_below(self, element, element_index=0):
		'''Get all elements of the POMSet that are strictly below `element`.

		Here weakly above means elements that are strictly less than 
		`element` in the POSET order.

		Parameters
		----------

		element : object
			The element of the POMSet to find elements below.

		element_index : int, optional
			In case there are multiple instances of element in the POMSet
			labels, the index of the element to find elements below;
			e.g. `element_index=3` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		labels_below : numpy ndarray
			A numpy array of label objects strictly below `element`
		'''
		label_index = np.where(self.labels == element)[0][element_index]
		return self.labels[(self.order[label_index] == -1)]

	def weakly_greater_than(self, element1, element2, element1_index=0, element2_index=0):
		'''Report whether `element1` is weakly greater than `element2`.

		In this case weakly greater than means not strictly less than.

		Parameters
		----------

		element1 : object
			The first element in the comparison

		element2 : object
			The second element in the comparison

		element1_index : int, optional
			In case there are multiple instances of element1 in the POMSet
			labels, the index of the element1 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		element2_index : int, optional
			In case there are multiple instances of element2 in the POMSet
			labels, the index of the element2 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		weakly_greater_than : boolean
			Whether `element1` is weakly greater than `element2`
		'''
		label_index1 = np.where(self.labels == element1)[0][element_index1]
		label_index2 = np.where(self.labels == element2)[0][element_index2]
		return self.order[label_index1, label_index2] >= 0

	def strictly_greater_than(self, element1, element2, element1_index=0, element2_index=0):
		'''Report whether `element1` is strictly greater than `element2`.

		Parameters
		----------

		element1 : object
			The first element in the comparison

		element2 : object
			The second element in the comparison

		element1_index : int, optional
			In case there are multiple instances of element1 in the POMSet
			labels, the index of the element1 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		element2_index : int, optional
			In case there are multiple instances of element2 in the POMSet
			labels, the index of the element2 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		strictly_greater_than : boolean
			Whether `element1` is strictly greater than `element2`
		'''
		label_index1 = np.where(self.labels == element1)[0][element_index1]
		label_index2 = np.where(self.labels == element2)[0][element_index2]
		return self.order[label_index1, label_index2] > 0

	def weakly_less_than(self, element1, element2, element1_index=0, element2_index=0):
		'''Report whether `element1` is weakly less than `element2`.

		In this case weakly less than means not strictly greater than.

		Parameters
		----------

		element1 : object
			The first element in the comparison

		element2 : object
			The second element in the comparison

		element1_index : int, optional
			In case there are multiple instances of element1 in the POMSet
			labels, the index of the element1 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		element2_index : int, optional
			In case there are multiple instances of element2 in the POMSet
			labels, the index of the element2 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		weakly_less_than : boolean
			Whether `element1` is weakly less than `element2`
		'''
		label_index1 = np.where(self.labels == element1)[0][element_index1]
		label_index2 = np.where(self.labels == element2)[0][element_index2]
		return self.order[label_index1, label_index2] <= 0

	def strictly_less_than(self, element1, element2, element1_index=0, element2_index=0):
		'''Report whether `element1` is strictly less than `element2`.

		Parameters
		----------

		element1 : object
			The first element in the comparison

		element2 : object
			The second element in the comparison

		element1_index : int, optional
			In case there are multiple instances of element1 in the POMSet
			labels, the index of the element1 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		element2_index : int, optional
			In case there are multiple instances of element2 in the POMSet
			labels, the index of the element2 ;
			e.g. `element_index=13` will select the third copy of element
			within the label list. (default 0)

		Returns
		-------

		strictly_less_than : boolean
			Whether `element1` is strictly less than `element2`
		'''
		label_index1 = np.where(self.labels == element1)[0][element_index1]
		label_index2 = np.where(self.labels == element2)[0][element_index2]
		return self.order[label_index1, label_index2] < 0

	def add_label(self, new_label):
		'''Add a new element to the POMSet. The added element will be
		unrelated to any other elements in the POMSet; to induce relations
		after using this method use the `add_dependency` or 
		`add_dependencies_from` functions.

		Parameters
		----------

		new_label : object
			The new element to add to the POMSet.
		'''
		new_label_array = np.empty(self.size + 1, dtype=object)
		new_label_array[:-1] = self.labels
		del self.labels
		self.labels = new_label_array
		self.labels[-1] = new_label

		self.size = len(self.labels)
		self.support.add(new_label)
		self.cardinality = len(self.support)

		new_order = np.zeros((self.size, self.size), dtype=np.int8)
		new_order[:-1][:-1] = self.order
		del self.order
		self.order = new_order

	def add_dependency(self, from_label, to_label, from_index=0, to_index=0):
		'''Add a new dependency relation to the POMSet. This states that
		`from_label` is strictly less than `to_label`. All other relations
		implicit from this will then be inferred and also added.

		Parameters
		----------

		from_label : object
			The lesser element of the new relation to add

		to_label : object
			The greater element of the new relation to add

		from_index : int, optional
			In case there are multiple instances of from_element in the POMSet
			labels, the index of the from_element ;
			e.g. `element_index=13` will select the third copy of from_element
			within the label list. (default 0)

		to_index : int, optional
			In case there are multiple instances of to_element in the POMSet
			labels, the index of the to_element ;
			e.g. `element_index=13` will select the third copy of to_element
			within the label list. (default 0)

		'''
		from_label_index = np.where(self.labels == from_label)[0][from_index]
		to_label_index = np.where(self.labels == to_label)[0][to_index]

		self.order[from_label_index, to_label_index] = -1
		self.order[to_label_index, from_label_index] = 1

		self.order[from_label_index, self._indices_strictly_above(to_label, to_index)] = -1
		self.order[to_label_index, self._indices_strictly_below(from_label, from_index)] = 1
