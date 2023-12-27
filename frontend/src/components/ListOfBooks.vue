<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!--bootswatch CDN-->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
        integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Books Library
          </h1>
          <hr />
          <br />
          <!-- Alert Message -->
          <b-alert variant="success" v-if="showMessage" show>
            {{ message }}
          </b-alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal:book-modal
          >
            Add Book
          </button>
          <br />
          <br />
          <table class="table table-hover">
            <!-- Table head -->
            <thead>
              <tr>
                <!-- Table Header cells -->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Read</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(book, index) in books" :key="index">
                <td>{{ book.title }}</td>
                <td>{{ book.genre }}</td>
                <td>
                  <span v-if="book.read">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" roles="group">
                    <button
                      type="button"
                      class="btn btn-info btn-sm"
                      v-b-modal.book-update-modal
                      @click="editBook(book)"
                    >
                      Update
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="removeBook(book)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy;. All Rights Reserved 2023.
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <b-modal
        ref="addBookModal"
        id="book-modal"
        title="Add a new book"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="submit" @reset="reset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addBookForm.title"
              required
              placeholder="Enter book"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-genre-group"
            label="Genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              v-model="addBookForm.genre"
              required
              placeholder="Enter Genre"
            >
            </b-form-input>
          </b-form-group>

          <!-- Checkbox -->
          <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addBookForm.read" id="form-check">
              <b-form-checkbox value="true">Read</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <!-- Buttons: submit and rest -->
          <div class="btns-wrap">
            <b-button type="reset" variant="outline-danger">Reset</b-button>
            <b-button type="submit" variant="outline-info">Submit</b-button>
          </div>
        </b-form>
      </b-modal>
      <b-modal
        ref="editBookModal"
        id="book-update-modal"
        title="Update"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="submitUpdate" @reset="resetUpdate" class="w-100">
          <b-form-group
            id="form-title-edit-group"
            label="Title:"
            label-for="form-title-edit-input"
          >
            <b-form-input
              id="form-title-edit-input"
              type="text"
              v-model="editForm.title"
              required
              placeholder="Enter book"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-genre-edit-group"
            label="Genre:"
            label-for="form-genre-edit-input"
          >
            <b-form-input
              id="form-genre-edit-input"
              type="text"
              v-model="editForm.genre"
              required
              placeholder="Enter Genre"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-read-edit-group">
            <b-form-checkbox-group v-model="editForm.read" id="form-checks">
              <b-form-checkbox value="true">Read</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button-group>
            <b-button type="reset" variant="outline-danger">Cancel</b-button>
            <b-button type="submit" variant="outline-info">Update</b-button>
          </b-button-group>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: "",
        genre: "",
        read: [],
      },
      editForm: {
        id: "",
        title: "",
        genre: "",
        read: [],
      },
    };
  },
  message: "",

  methods: {
    // GET Function
    getBooks() {
      const path = "http://localhost:5000/books";
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // POST Function
    addBook(payload) {
      const path = "http://localhost:5000/books";
      axios
        .post(path, payload)
        .then(() => {
          this.getBooks();
          // Message alert
          this.message = "Book Added!";
          // To show message
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = "";
      this.addBookForm.genre = "";
      this.addBookForm.read = [];
      this.editForm.id = "";
      this.editForm.title = "";
      this.editForm.genre = "";
      this.editForm.read = [];
    },
    submit(e) {
      e.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        genre: this.addBookForm.genre,
        read,
      };
      this.addBook(payload);
      this.initForm();
    },
    reset(e) {
      e.preventDefault();
      this.initForm();
    },
    submitUpdate(e) {
      e.preventDefault();
      this.$refs.editBookModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editBookForm.title,
        genre: this.editBookForm.genre,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },
    resetUpdate(e) {
      e.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks();
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = "Book Updated!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    deleteBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .delete(path)
        .then(() => {
          this.getBooks();
          this.message = "Book Removed!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    // Handle update button
    editBook(book) {
      this.editForm = book;
    },
    // Handle delete button
    removeBook(book) {
      this.deleteBook(book.id);
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

<style>
.btns-wrap {
  display: flex;
  align-items: center;
  justify-content: end;
  gap: 20px;
}
</style>
