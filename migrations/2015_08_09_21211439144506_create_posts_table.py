from orator.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.integer('tag_id')
            table.string('title', 100)
            table.text('content')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')
