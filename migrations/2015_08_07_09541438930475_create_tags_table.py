from orator.migrations import Migration


class CreateTagsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tags') as table:
            table.increments('id')
            table.string('label')
            table.integer('post_id')
            table.timestamps()

            table.foreign('post_id').references('id').on('posts')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tags')
