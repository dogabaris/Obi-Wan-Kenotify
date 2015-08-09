from orator.migrations import Migration


class RenameAuthorToUserId(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('posts') as table:
            table.rename_column('author', 'user_id')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('posts') as table:
            pass
