from orator.migrations import Migration


class AddPublishedDateToPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('posts') as table:
            table.timestamp('published_at').nullable()  # Cannot add a NOT NULL column with default value NULL

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('posts') as table:
            table.drop_column('published_at')
