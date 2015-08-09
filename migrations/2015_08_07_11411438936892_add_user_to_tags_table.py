from orator.migrations import Migration


class AddUserToTagsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('tags') as table:
            table.integer('user_id').default(0)

            table.foreign('user_id').references('id').on('users')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('tags') as table:
            self.schema.drop_column('user_id')
