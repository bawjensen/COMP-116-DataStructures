#include <iostream>
#include <algorithm>

using namespace std;

class Node {
private:
  int cargo;
  Node* next;
public:
  Node(int data) { cargo = data; next = NULL; };
  int getCargo() { return cargo; };
  void setCargo(int data) { cargo = data; };
  Node* getNext() { return next; };
  void setNext(int data) { next = new Node(data); };
  void setNodeNext(Node* node) { next = node; };
};

class LinkedList {
private:
  Node* head;
public:
  LinkedList() { head = NULL; };
  void displacement_insert(int);
  void relink_insert(int);
  void insert(int);
  void print_container();
};

void LinkedList::displacement_insert(int data) {
  if (head == NULL) {
    head = new Node(data);
  }
  else {

    Node* itNode = head;
    bool atEnd = false;

    while (!atEnd) {
      if (itNode->getNext() == NULL) {
        atEnd = true;
      }

      if (data < itNode->getCargo()) {
        int temp = itNode->getCargo();
        itNode->setCargo(data);
        cout << "shifting " << temp << " for " << data << endl;
        data = temp;
      }

      if (!atEnd) {
        itNode = itNode->getNext();
      }
    }

    itNode->setNext(data);
  }
}

void LinkedList::relink_insert(int data) {
  if (head == NULL) {
    head = new Node(data);
  }

  else {
    Node* itNode = head;

    while (itNode->getNext() != NULL and data > itNode->getNext()->getCargo()) {
      //cout << "looped" << endl;
      itNode = itNode->getNext();
    }

    if (itNode == head and data < head->getCargo()) {
      Node* splitNode = head;
      head = new Node(data);
      head->setNodeNext(splitNode);
    }
    else if (data < itNode->getCargo() and itNode->getNext() == NULL) {
      Node* splitNode = new Node(itNode->getCargo());
      itNode->setCargo(data);
      itNode->setNodeNext(splitNode);
    }
    else if (itNode->getNext() != NULL and data < itNode->getNext()->getCargo()) {
      Node* splitNode = itNode->getNext();
      itNode->setNext(data);
      itNode->getNext()->setNodeNext(splitNode);
    }
    else if (itNode->getNext() == NULL) {
      itNode->setNext(data);
    }
  }
}

void LinkedList::print_container() {
  Node* itNode = head;

  while (itNode != NULL) {
    cout << itNode->getCargo() << " ";
    itNode = itNode->getNext();
  }
  cout << endl;
}

void LinkedList::insert(int data) {
  relink_insert(data);
}

int main() {
  LinkedList ll;

  srand(time(NULL));

  for (int i = 0; i < 30; i++) {
    int random = rand() % 100;
    ll.insert(random);
    cout << random << endl;
  }

  cout << endl;

  ll.print_container();
}