from orator.migrations import Migration


class AddTagsToPostTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('posts') as table:
            table.integer('tag_id').default(0)

            table.foreign('tag_id').references('id').on('tags')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('posts') as table:
            self.schema.drop_column('tag_id')
