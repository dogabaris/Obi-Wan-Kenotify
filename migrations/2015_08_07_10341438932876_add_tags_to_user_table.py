from orator.migrations import Migration


class AddTagsToUserTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.integer('tag_id').default(0)

            table.foreign('tag_id').references('id').on('tags')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            self.schema.drop_column('tag_id')
